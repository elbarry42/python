#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, model_validator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(
        default=None,
        max_length=500,
    )
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        # 1. ID doit commencer par AC
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC'"
            )

        # 2. Physical → must be verified
        if self.contact_type == ContactType.physical:
            if not self.is_verified:
                raise ValueError(
                    "Physical contact must be verified"
                )

        # 3. Telepathic → ≥ 3 witnesses
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )

        # 4. Signal > 7 → message obligatoire
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError(
                    "Strong signals require a message"
                )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    # ✅ VALID
    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-01-01T12:00:00",
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )

    print("Valid contact report:")
    print(f"ID: {valid_contact.contact_id}")
    print(f"Type: {valid_contact.contact_type}")
    print(f"Location: {valid_contact.location}")
    print(f"Signal: {valid_contact.signal_strength}/10")
    print(f"Duration: {valid_contact.duration_minutes} minutes")
    print(f"Witnesses: {valid_contact.witness_count}")
    print(f"Message: {valid_contact.message_received}")

    print("=" * 40)

    # ❌ INVALID
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-01-01T12:00:00",
            location="Unknown",
            contact_type="telepathic",
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=1,  # erreur
        )
    except Exception as error:
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
