from .app import (
    module,
)


@module.route('/hook', methods=['POST'])
def hook():
    pass
