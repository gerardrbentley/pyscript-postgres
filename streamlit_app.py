import json
import httpx
import asyncio
import streamlit as st
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

st.header("Streaming Postgres Inserts to Streamlit!")


async def main():
    client = httpx.AsyncClient()
    log.info("Running main")
    async with client.stream(
        "GET", "https://notes-api.gerardbentley.com/listen_notes", timeout=None
    ) as response:
        log.info("Listening")
        async for chunk in response.aiter_bytes():
            log.info(f"processing: {str(chunk)}")
            st.json(json.loads(chunk))


asyncio.run(main())
