# checks/__init__.py
# Package initializer for Sanity First validator checks.
# Enables imports like 'from checks import ethics_llm'.
# (Arithmetic note: Like a "zero" base in numeral systems—enables modular ops; Wikipedia: en.wikipedia.org/wiki/Arithmetic)
# GDPR note: Ensures structured, transparent code—respect data rights (gdpr.eu).

# Optional: Import all plugins for convenience (uncomment if needed)
# from .ethics_llm import check as ethics_check
# from .law_llm import check as law_check
# from .facts_llm import check as facts_check
# from .logic_llm import check as logic_check

__all__ = ['ethics_llm', 'law_llm', 'facts_llm', 'logic_llm', 'llm_bridge']
