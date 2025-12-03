from mcp.server.fastmcp import FastMCP

#Create the FastMCP server instance
mcp = FastMCP("sritaj_info_server")

@mcp.tool()
def get_sritaj_info():
    """
    Returns information about Sritaj including name, about me, and roles.
    """
    return {
        "name": "Sritaj",
        "about_me": "I've spent the last decade breaking software to help build it better, evolving from manual testing to architecting complex automation frameworks. My approach blends the discipline of 'Shift Left' engineering with the potential of AI, using tools like Playwright and LangChain to make testing smarter, not just faster. I believe quality is a team sport, and I'm passionate about bridging the gap between developers and QA to bake reliability into every stage of development. I'm on a mission to prove that AI doesn't replace human judgment; it supercharges it to deliver software that users love. While I thrive as a hands-on contributor, I naturally step up to lead when the team needs direction, using my Scrum Master hat to unblock barriers and foster a culture of ownership.",
        "role": ["Bug Fixer & Developer", "Quality Engineering", "Scrum Master", "CI/CD & Automation Enthusiast", "AI Engineer in Making"],
    }