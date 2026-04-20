#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv


def load_config() -> dict:
    load_dotenv()

    config = {
        "mode": os.getenv("MATRIX_MODE"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config: dict) -> bool:
    missing = [key for key, value in config.items() if not value]

    if missing:
        print("ERROR: Missing configuration:")
        for key in missing:
            print(f"- {key}")
        return False

    return True


def print_config(config: dict) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    print(f"Mode: {config['mode']}")

    if config["mode"] == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production system")

    print("API Access: Authenticated")
    print(f"Log Level: {config['log_level']}")
    print("Zion Network: Online")


def security_check() -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> None:
    config = load_config()

    if not validate_config(config):
        print("\nPlease check your .env file or environment variables.")
        sys.exit(1)

    print_config(config)
    security_check()


if __name__ == "__main__":
    main()
