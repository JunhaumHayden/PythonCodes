# Problema de importaçao de arquivos em python

```python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
```
  [video](https://www.youtube.com/watch?v=bCQrN8qCxiU)


