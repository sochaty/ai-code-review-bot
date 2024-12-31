# src/code_analyzer/analyzer.py

import io
import os
import pylint.lint
from pylint.reporters.text import TextReporter


class CodeAnalyzer:
    def analyze(self, code):
        results = []

        # Set up a string buffer to capture pylint output
        output_buffer = io.StringIO()
        reporter = TextReporter(output_buffer)

        # Write code to a temporary file
        temp_file_name = "temp_code.py"
        with open(temp_file_name, "w", encoding="utf-8") as temp_file:
            temp_file.write(code)

        try:
            # Run pylint on the temporary file
            # Disabling "C" (convention) and "R" (refactor)
            pylint_opts = [temp_file_name, "--disable=C,R",
                           "--enable=missing-module-docstring"]
            pylint.lint.Run(pylint_opts, reporter=reporter, exit=False)

            # Capture the results from the buffer and process them
            output_buffer.seek(0)
            for line in output_buffer.readlines():
                # Only capture meaningful linting messages
                if line.strip() and not line.startswith(("********", "Your code")):
                    results.append(line.strip())
        finally:
            # Clean up the temporary file
            os.remove(temp_file_name)

        return results
