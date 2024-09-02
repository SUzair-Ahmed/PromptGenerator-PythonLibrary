from myprompt import mylibrary as ml

def main():
    # Create an instance of the PromptGenerator
    prompt_generator = ml.PromptGenerator()

    # Get categories
    categories = prompt_generator.get_categories()
    print("Categories:", categories)

    # Choose a category
    selected_category = input("Select a category from the list: ")

    # Get sub-categories for the selected category
    sub_categories = prompt_generator.get_sub_categories(selected_category)
    print("Sub-Categories:", sub_categories)

    # Choose a sub-category
    selected_sub_category = input("Select a sub-category from the list: ")

    # Get templates for the selected sub-category
    templates = prompt_generator.get_templates(selected_category, selected_sub_category)
    print("Templates:", templates)

    # Choose a template
    selected_template = input("Select a template from the list: ")

    # Get fields required for the selected template
    fields = prompt_generator.get_template_fields(selected_template)
    print("Fields required:", fields)

    # Collect user inputs based on the template fields
    user_inputs = prompt_generator.collect_user_inputs(fields)

    # Generate the prompt
    prompt = prompt_generator.generate_prompt(selected_category, selected_sub_category, selected_template, user_inputs)
    print("Generated Prompt:", prompt)

if __name__ == "__main__":
    main()
