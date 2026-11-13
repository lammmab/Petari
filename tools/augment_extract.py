#!/usr/bin/env python3
import os, subprocess, sys
from pathlib import Path

tools = Path(__file__).resolve().parent.parent / "external" / "augment" / "tools"
env = dict(os.environ)
env["PYTHONPATH"] = os.pathsep.join(filter(None, [str(tools), env.get("PYTHONPATH")]))
sys.exit(subprocess.call(
    [sys.executable, "-u", str(tools / "extractor" / "extract.py"), *sys.argv[1:]],
    env=env,
))
