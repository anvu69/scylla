from scylla.providers.plain_text_provider import PlainTextProvider


class GithubProvider(PlainTextProvider):

    def urls(self) -> [str]:
        return [
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt'
        ]
