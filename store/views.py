from django.shortcuts import render, redirect
from .models import Product
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key securely
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to generate tags using OpenAI
def generate_tags(description):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate 5 relevant tags for a product with the following description: {description}",
            max_tokens=50
        )
        tags = response.choices[0].text.strip().split(',')
        return [tag.strip() for tag in tags]
    except Exception as e:
        print(f"Error generating tags: {e}")
        return ["default_tag"]  # Return a default tag in case of an error

# View to add a product
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = float(request.POST['price'])
        category = request.POST['category']
        
        # Generate tags using OpenAI
        tags = generate_tags(description)
        
        # Create and save the product with tags
        product = Product(name=name, description=description, price=price, category=category, tags=tags)
        product.save()
        
        return redirect('product_list')  # Redirect to the product list page
    
    return render(request, 'add_product.html')

# View to display the product list
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})