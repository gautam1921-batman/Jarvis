import os
import json
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from groq import Groq

# PRE-PRODUCTION MONETIZATION BLOCK
# Stripe provides a Python library (pip install stripe). For our sandbox layout,
# we are building a secure payment simulation router that mimics Stripe's operational webhook flow.
app = FastAPI(title="Lander AI SaaS Engine")

templates = Jinja2Templates(directory="templates")

def call_groq_seo_generator(business_name, location, service, usp):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {
            "hero_headline": f"Professional {service} Services in {location}",
            "hero_subheadline": f"Top-rated quality and dedicated care from the expert team at {business_name}.",
            "value_paragraph": f"We provide premier workmanship across {location}. Contact us today to handle your tasks safely.",
            "usp_paragraph": f"Proudly delivering unmatched reliability built around: {usp}."
        }

    client = Groq(api_key=api_key)
    system_prompt = (
        "You are an expert conversion copywriter and SEO engineer. Generate high-converting website content "
        "tailored for local businesses. You must output ONLY a valid raw JSON object. Do not include markdown code ticks, "
        "introductions, or conversational summaries. The JSON layout must have exactly these keys:\n"
        '{"hero_headline": "...", "hero_subheadline": "...", "value_paragraph": "...", "usp_paragraph": "..."}'
    )
    user_prompt = f"Business Name: {business_name}\nLocation: {location}\nService: {service}\nUnique Selling Point: {usp}"

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.4
        )
        return json.loads(response.choices.message.content.strip())
    except Exception:
        return {
            "hero_headline": f"Premium {service} in {location}",
            "hero_subheadline": f"The dependable choice for homeowners and local businesses at {business_name}.",
            "value_paragraph": f"Serving the {location} community with dedication, expert tools, and premium care.",
            "usp_paragraph": f"Built around our promise: {usp}."
        }

@app.get("/", response_class=HTMLResponse)
async def load_input_page(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/generate", response_class=HTMLResponse)
async def handle_generation_form(
    request: Request,
    business_name: str = Form(...),
    location: str = Form(...),
    service: str = Form(...),
    usp: str = Form(...)
):
    ai_content = call_groq_seo_generator(business_name, location, service, usp)
    return templates.TemplateResponse(
        request=request, 
        name="landing_page.html", 
        context={
            "business_name": business_name,
            "location": location,
            "service": service,
            "usp": usp,
            "ai_data": ai_content
        }
    )

# 💳 COMMERCIAL PAYMENT GATEWAY ROUTE
@app.post("/api/v1/checkout")
async def create_secure_payment_session():
    """
    Simulates a live Stripe Checkout pipeline instance. 
    In production, this talks to stripe.checkout.Session.create()
    """
    # Directing the user to your integrated payment portal link structure
    checkout_url = "https://stripe.com"
    
    # We return a JSON link response that our frontend button will read instantly
    return JSONResponse(content={"checkout_url": checkout_url, "status": "pending_payment"})
