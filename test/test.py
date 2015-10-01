import os

from qubell.api.testing import *

@environment({
    "default": {}
})
class OracleTestCase(BaseComponentTestCase):
    name = "component-oracle-db"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]
    @classmethod
    def timeout(cls):
        return 60

    @instance(byApplication=name)
    def test_database_port(self, instance):
        import socket
        host = instance.returnValues['oracledb.db-host']
        port = instance.returnValues['oracledb.db-port']
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((str(host), int(port)))
        assert result == 0
