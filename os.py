def _create_os_config_from_inputs(self, api_key, api_host, api_port, api_ca):
        """
         Create Openshift Client config from inputted values
        :param api_key:
        :param api_host:
        :param api_port:
        :param api_ca:
        :return:
        """
        from openshift import client
        oclient_config = client.Configuration()
        oclient_config.host = self._get_host_name(api_host, api_port)
        oclient_config.api_key['authorization'] = self._get__bearer_token(api_key)
        oclient_config.ssl_ca_cert = self._get_ca_cert_filename(api_ca)
        # add user kubernetes attributes
        oapi = client.OapiApi(oclient_config)
        return oapi
