from typing import Any
from data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor
)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            found = False

            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    found = True
                    break

            if not found:
                print(
                    "DataStream error "
                    f"- Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")

            total = proc._counter
            remaining = len(proc._storage)

            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


# =========================
# TEST MAIN (SUJET)
# =========================

def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    # Init
    print("\nInitialize Data Stream...")
    stream = DataStream()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    # Register only Numeric first
    print("\nRegistering Numeric Processor")
    num = NumericProcessor()
    stream.register_processor(num)

    # First batch
    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print(
        "\nSend first batch of data on stream: "
        f"{batch}"
    )
    stream.process_stream(batch)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    # Register remaining processors
    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()

    stream.register_processor(text)
    stream.register_processor(log)

    # Send same batch again
    print("\nSend the same batch again")
    stream.process_stream(batch)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    # Consume data
    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        num.output()

    for _ in range(2):
        text.output()

    for _ in range(1):
        log.output()

    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
