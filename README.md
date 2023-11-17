# Litestar piccolo

## Installation

```shell
pip install litestar-piccolo
```

## Usage

Here is a basic application that demonstrates how to use the plugin.

```python
from __future__ import annotations

from litestar import Litestar

from litestar_piccolo import PiccoloPlugin

piccolo = PiccoloPlugin()
app = Litestar(plugins=[piccolo])

```
