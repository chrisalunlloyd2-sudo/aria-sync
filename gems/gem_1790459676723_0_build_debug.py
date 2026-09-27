'''Auto-extracted gem from session-2026-09-19T21-54-17c4f12f.jsonl (gemini-3.1-flash-lite)
Confidence: 0.99 | Tags: ['build', 'debug', 'sync', 'shell', 'python']
Timestamp: 2026-09-20T14:44:04.099Z
'''
import asyncio

async def run_stage_async(self, oomph: str):
    # Use direct list execution instead of shell=True
    cmd_args = self.command.split() 
    
    process = await asyncio.create_subprocess_exec(
        *cmd_args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    try:
        # Wait with timeout without blocking the main event loop
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=self.timeout)
        self.exit_code = process.returncode
        self.stdout = stdout.decode()
        self.stderr = stderr.decode()
    except asyncio.TimeoutError:
        process.kill()
        self.stderr = "[TIMEOUT]"