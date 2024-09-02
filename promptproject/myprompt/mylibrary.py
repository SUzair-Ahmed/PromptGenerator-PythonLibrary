class PromptGenerator:
    def __init__(self):
        self.templates = {
            "LinkedIn Bio Generator": ["Job Description", "Desired Words Count"],
            "LinkedIn Post Caption": ["Post Topic", "Tone"],
            "Instagram Bio Generator": ["About Your Self", "Your profession"],
            "Instagram Post Caption": ["What your post about Define your post in under one line.", "Desired Words Count"],
            "AI Roadmap Generator": ["Learning Timeframe", "Target Skill Level"],
            "AI Quiz Generator": ["How many question you want on AI", "Difficulty Level"],
            "Web Development Roadmap Generator": ["Learning Timeframe", "Target Skill Level"],
            "Web Development Projects": ["How many Projects you want?", "What should be the difficulty level of projects?"],
            "SEO Strategy Outline": ["Target Audience age?", "Competitor"],
            "SEO Content Calendar": ["Content Topic", "Posting Frequency"],
            "Content Plan": ["Audience Segment", "Content Goals"],
            "Content Plan": ["Industry or Niche", "Target Audience"],
        }

    def get_categories(self):
        return ["Social Media", "Technology", "Marketing"]

    def get_sub_categories(self, category):
        if category == "Social Media":
            return ["Instagram", "LinkedIn"]
        elif category == "Technology":
            return ["AI", "Web Development"]
        elif category == "Marketing":
            return ["SEO", "Content Marketing"]
        return []

    def get_templates(self, category, sub_category):
        if category == "Social Media" and sub_category == "LinkedIn":
            return ["LinkedIn Bio Generator", "LinkedIn Post Caption"]
        elif category == "Social Media" and sub_category == "Instagram":
            return ["Instagram Bio Generator", "Instagram Post Caption"]
        elif category == "Technology" and sub_category == "AI":
            return ["AI Roadmap Generator", "AI Quiz Generator"]
        elif category == "Technology" and sub_category == "Web Development":
            return ["Web Development Roadmap Generator", "Web Development Projects"]
        elif category == "Marketing" and sub_category == "SEO":
            return ["SEO Strategy Outline", "SEO Content Calendar"]
        elif category == "Marketing" and sub_category == "Content Marketing":
            return ["Content Plan", "Content Plan"]
        return []

    def get_template_fields(self, template):
        return self.templates.get(template, [])

    def generate_prompt(self, category, sub_category, template, user_inputs):
        field_values = [f"{field}: {user_inputs.get(field, 'N/A')}" for field in self.templates.get(template, [])]
        prompt = (f"Craft a comprehensive and highly tailored output for the selected template '{template}' "
                  f"within the '{category}' category and '{sub_category}' sub-category. "
                  f"Utilize the following parameters: {', '.join(field_values)} to ensure the result is "
                  f"precisely aligned with the user's goals. The output should be not only concise and impactful "
                  f"but also optimized to meet industry standards and the specific needs of the target audience.")
        return prompt

    def collect_user_inputs(self, fields):
        user_inputs = {}
        for field in fields:
            user_input = input(f"Please provide the {field}: ")
            user_inputs[field] = user_input
        return user_inputs
