"""Run the Phase 13 Flask application."""

from enterprise_rag.api.app import (
    create_app,
)


def main():
    app = create_app()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
    )


if __name__ == "__main__":
    main()
