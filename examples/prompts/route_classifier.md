# Route Classifier

You are analyzing a web page to classify it into a specific route category. Please analyze the following information and return a JSON object with two properties:

1. "category": The route category (e.g., "auth", "dashboard", "product", "landing", "profile", "settings", "admin", "checkout", "search", etc.)
2. "description": A brief description of what this route is used for

URL: {url}
Page Title: {pageTitle}
Page Content: {pageContent}

Return ONLY a valid JSON object like this: {"category": "category-name", "description": "brief description"}