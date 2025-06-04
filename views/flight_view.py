import math
import pygame

from config import Settings
from views.base_view import BaseView
from services.resource_service import ResourceService

from models.star_system import StarSystem
from models.ship import Ship


class FlightView(BaseView):
    """Top‑down space‑flight renderer."""

    def __init__(
        self,
        screen: pygame.Surface,
        system: StarSystem | None = None,
        ship: Ship | None = None,
    ) -> None:
        super().__init__(screen)
        self.system = system
        self.ship = ship

        res = ResourceService(Settings())
        self.star_img = res.get_image("star.png")
        self.planet_img = res.get_image("planet.png")
        self.ship_img = res.get_image("ship.png")

    def render(self) -> None:
        # a) draw black background
        self.screen.fill("black")

        if not self.system or not self.ship:
            return

        centre = self.screen.get_width() // 2, self.screen.get_height() // 2

        # b) iterate over system.planets and blit sprite at ship.position + planet_screen_offset
        for planet in self.system.planets:
            radius = planet.orbit_radius_km * 0.001
            offset = (
                math.cos(planet.theta) * radius,
                math.sin(planet.theta) * radius,
            )
            pos = (
                centre[0] + self.ship.position.x + offset[0],
                centre[1] + self.ship.position.y + offset[1],
            )
            self.screen.blit(self.planet_img, pos)

        # c) draw star at (0,0) for now
        self.screen.blit(self.star_img, (0, 0))

        # d) blit ship sprite at screen-centre
        ship_rect = self.ship_img.get_rect(center=centre)
        self.screen.blit(self.ship_img, ship_rect)
