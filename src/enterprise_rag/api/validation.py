"""Request validation for the Phase 13 Flask API."""


class RequestValidationError(ValueError):
    """Raised when an API request is invalid."""


def validate_query_request(payload) -> dict:
    """Validate and normalize a query request."""

    if not isinstance(payload, dict):
        raise RequestValidationError(
            "request body must be a JSON object"
        )

    user_id = payload.get("user_id")
    question = payload.get("question")

    if not isinstance(user_id, str) or not user_id.strip():
        raise RequestValidationError(
            "user_id must be a non-empty string"
        )

    if not isinstance(question, str) or not question.strip():
        raise RequestValidationError(
            "question must be a non-empty string"
        )

    top_k = payload.get("top_k", 5)

    if (
        not isinstance(top_k, int)
        or isinstance(top_k, bool)
        or top_k <= 0
    ):
        raise RequestValidationError(
            "top_k must be a positive integer"
        )

    return {
        "user_id": user_id.strip(),
        "question": question.strip(),
        "top_k": top_k,
    }
