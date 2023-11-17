from __future__ import annotations

from litestar import Litestar

from litestar_piccolo import PiccoloPlugin

piccolo = PiccoloPlugin()
app = Litestar(plugins=[piccolo])
