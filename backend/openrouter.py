"""OpenRouter API client for making LLM requests."""

import httpx
from typing import List, Dict, Any, Optional
from .config import OPENROUTER_API_KEY, OPENROUTER_API_URL


async def query_model(
    model: str,
    messages: List[Dict[str, str]],
    timeout: float = 120.0,
    temperature: Optional[float] = None,
    reasoning_effort: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Query a single model via OpenRouter API.
    """
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
    }

    # Eğer dışarıdan bir sıcaklık değeri gönderildiyse payload'a ekle
    if temperature is not None:
        payload["temperature"] = temperature

    # Akıl yürütme parametresini sadece destekleyen OpenAI modelleri için ekle
    if reasoning_effort and ("gpt-" in model or "o1" in model or "o3" in model):
        payload["reasoning_effort"] = reasoning_effort

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                OPENROUTER_API_URL,
                headers=headers,
                json=payload
            )
            response.raise_for_status()

            data = response.json()
            message = data['choices'][0]['message']

            return {
                'content': message.get('content'),
                'reasoning_details': message.get('reasoning_details')
            }

    except Exception as e:
        print(f"Error querying model {model}: {e}")
        return None


async def query_models_parallel(
    models: List[str],
    messages: List[Dict[str, str]],
    temperature: Optional[float] = None,
    reasoning_effort: Optional[str] = None
) -> Dict[str, Optional[Dict[str, Any]]]:
    """
    Query multiple models in parallel with specific parameters.
    """
    import asyncio

    # Parametreleri tekil model sorgularına pasla
    tasks = [
        query_model(model, messages, temperature=temperature, reasoning_effort=reasoning_effort) 
        for model in models
    ]

    # Wait for all to complete
    responses = await asyncio.gather(*tasks)

    # Map models to their responses
    return {model: response for model, response in zip(models, responses)}