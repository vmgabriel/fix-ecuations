#!/urs/bin/env python
# -*- coding: utf-8 -*-

"""
Archivo para Metodo principal

@author: Andres Aguirre - Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

from cli import Cli
from libs import *

if __name__ == "__main__":
    """
    Metodo Principal

    @note: Cargador Principal correra Cli.run() que estará en cli/
    """
    run=Cli()
    run.run()
