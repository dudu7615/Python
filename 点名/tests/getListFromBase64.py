from pathlib import Path
import base64

file = Path(__file__).parent.parent / "names"

print(
    type(
        eval(
            base64.decodebytes(file.read_text(encoding="utf-8").encode("utf-8")).decode(
                "utf-8"
            )
        )
    )
)
