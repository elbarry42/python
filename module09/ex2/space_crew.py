#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import List
from enum import Enum


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember]
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            member.rank in (Rank.captain, Rank.commander)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Captain or Commander"
            )

        if self.duration_days > 365:
            experienced = [
                m for m in self.crew
                if m.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError(
                    "Not enough experienced crew"
                )

        if any(not m.is_active for m in self.crew):
            raise ValueError(
                "All crew members must be active"
            )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2024-06-01T10:00:00"),
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=40,
                specialization="Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=30,
                specialization="Engineering",
                years_experience=6,
            ),
        ],
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")

    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank}) "
            f"- {member.specialization}"
        )

    print("=" * 40)

    try:
        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Bad Mission",
            destination="Mars",
            launch_date=datetime.fromisoformat("2024-06-01T10:00:00"),
            duration_days=100,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="C004",
                    name="Bob",
                    rank=Rank.officer,
                    age=25,
                    specialization="Tech",
                    years_experience=1,
                )
            ],
        )
    except Exception as error:
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
