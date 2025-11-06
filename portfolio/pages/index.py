import reflex as rx

# Import all sections
from ..components.common import navbar, footer
from ..components.hero_section import hero_section
from ..components.about_section import about_section
from ..components.services_section import services_section
from ..components.portfolio_section import portfolio_section
from ..components.contact_section import contact_section

def index_page() -> rx.Component:
    """
    Main index page component.
    """
    # The main page is a Vstack of all sections
    return rx.box(
        # The navbar is sticky and positioned on top
        navbar.navbar(),
        hero_section(),
        about_section(),
        services_section(),
        portfolio_section(),
        contact_section(),
        footer.footer(),
        width="100%",
        spacing="0",
        bg="var(--bg)",
    )
