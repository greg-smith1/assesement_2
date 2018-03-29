#!/usr/bin/env python3

from core import omnibus

if __name__ == '__main__':
    # local environment
    omnibus.run(debug=True)
    # Production Environment
    #omnibus.run(host='0.0.0.0')
