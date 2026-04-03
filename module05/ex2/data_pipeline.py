from typing import Protocol
from data_stream import DataStream
from data_processor import (
    NumericProcessor,
    TextProcessor,
    LogProcessor
)


class ExportPlugin(Protocol):
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        ...


class CSVExport:
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        values = [value for _, value in data]

        print("CSV Output:")
        print(",".join(values))


class JSONExport:
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        print("JSON Output:")

        result: dict[str, str] = {}

        for index, value in data:
            result[f"item_{index}"] = value

        print(result)


class PipelineDataStream(DataStream):
    def output_pipeline(
        self,
        nb: int,
        plugin: ExportPlugin
    ) -> None:
        for proc in self.processors:
            extracted: list[tuple[int, str]] = []

            for _ in range(nb):
                try:
                    extracted.append(proc.output())
                except Exception:
                    break

            if extracted:
                plugin.process_output(extracted)


# =========================
# TEST MAIN (SUJET)
# =========================

def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    # Init
    print("\nInitialize Data Stream...")
    stream = PipelineDataStream()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    # Register processors
    print("\nRegistering Processors")
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    stream.register_processor(num)
    stream.register_processor(text)
    stream.register_processor(log)

    # First batch
    batch1 = [
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
        f"{batch1}"
    )
    stream.process_stream(batch1)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    # CSV export
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExport()
    stream.output_pipeline(3, csv_plugin)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    # Second batch
    batch2 = [
        21,
        [
            "I love AI",
            "LLMs are wonderful",
            "Stay healthy"
        ],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print(
        "\nSend another batch of data: "
        f"{batch2}"
    )
    stream.process_stream(batch2)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    # JSON export
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExport()
    stream.output_pipeline(5, json_plugin)

    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
