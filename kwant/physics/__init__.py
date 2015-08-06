# Copyright 2011-2013 Kwant authors.
#
# This file is part of Kwant.  It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# http://kwant-project.org/license.  A list of Kwant authors can be found in
# the AUTHORS file at the top-level directory of this distribution and at
# http://kwant-project.org/authors.

"""Physics-related algorithms"""

# Merge the public interface of all submodules.
__all__ = []
for module in ['leads', 'dispersion', 'noise']:
    exec('from . import {0}'.format(module))
    exec('from .{0} import *'.format(module))
    exec('__all__.extend({0}.__all__)'.format(module))
