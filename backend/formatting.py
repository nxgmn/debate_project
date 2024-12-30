def format_response_openai(response):
    """Formats the response and metadata for better readability."""
    # Handle AIMessage or similar objects directly
    if hasattr(response, 'content'):
        content = response.content
    else:
        content = response.get("content", "[No content available]")  # Fallback for other response types

    return f"""
    **Response:**
    {content}
    """

def format_response_claude(response):
    """
    Formats the response from Claude AI into a readable format.

    Args:
        response: The response object from Claude AI.

    Returns:
        str: The formatted response content.
    """
    # Extract the content, handling cases where it's wrapped in a TextBlock
    try:
        if isinstance(response.content, list):  # Handles responses wrapped in objects
            content = "\n".join(block.text for block in response.content if hasattr(block, "text"))
        else:
            content = response.content if hasattr(response, "content") else "No content available."
    except AttributeError:
        content = "No content available."

    # Format the output
    formatted_response = f"""
    **Response:**
    {content.strip()}
    """
    return formatted_response



def format_response_gemini(response):
    """
    Formats the response provided by the Gemini LLM for better readability.

    Args:
        response (AIMessage): The AIMessage object returned by Gemini LLM.

    Returns:
        str: A formatted string representation of the Gemini response.
    """
    try:
        # Extract content and metadata
        content = getattr(response, "content", "No content available.")

        # Return formatted response
        return f"""
        **Response:**
        {content.strip()}
        """
    except AttributeError as e:
        return f"Error formatting Gemini response: {e}"
