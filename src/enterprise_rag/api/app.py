"""Flask application for the Secure RAG tutorial."""

from flask import Flask, jsonify, request

from enterprise_rag.api.query_service import (
    process_query,
)
from enterprise_rag.api.validation import (
    RequestValidationError,
    validate_query_request,
)


def create_app() -> Flask:
    """Create and configure the Flask application."""

    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(
            {
                "status": "ok",
                "service": "enterprise-rag",
            }
        )

    @app.post("/api/query")
    def query():
        try:
            payload = request.get_json(
                silent=True
            )

            validated = (
                validate_query_request(
                    payload
                )
            )

            result = process_query(
                user_id=validated["user_id"],
                question=validated["question"],
                top_k=validated["top_k"],
            )

            return jsonify(result)

        except RequestValidationError as exc:
            return (
                jsonify(
                    {
                        "error": "invalid_request",
                        "message": str(exc),
                    }
                ),
                400,
            )

        except KeyError:
            return (
                jsonify(
                    {
                        "error": "unknown_identity",
                        "message": (
                            "The requested identity "
                            "could not be resolved."
                        ),
                    }
                ),
                404,
            )

        except Exception:
            app.logger.exception(
                "Secure RAG query failed"
            )

            return (
                jsonify(
                    {
                        "error": "internal_error",
                        "message": (
                            "The Secure RAG request "
                            "could not be completed."
                        ),
                    }
                ),
                500,
            )

    return app
