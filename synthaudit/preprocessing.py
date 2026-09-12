"""Bounded document preprocessing using a focused LangChain component."""

from langchain_text_splitters import RecursiveCharacterTextSplitter

_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=1_500,
    chunk_overlap=150,
    separators=["\n\n", "\n", ". ", " ", ""],
)


def split_method_text(text: str) -> list[str]:
    """Split accepted text into traceable chunks; no model or external API is called."""
    return _SPLITTER.split_text(text)
