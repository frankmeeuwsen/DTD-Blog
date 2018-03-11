require 'uri'
require 'net/http'

url = URI("https://api.pinboard.in/v1/posts/update")
http = Net::HTTP.new(url.host, url.port)

$conf = {}
$conf['debug'] = true


class Utils
  def debug_msg(message,sticky = true)
    if $conf['debug']
      $stderr.puts message
    end
  end
end

util = Utils.new


request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer frankmeeuwsen:345EDBF89C7279603302'
request["Cache-Control"] = 'no-cache'
request["Postman-Token"] = 'cc9ee4c1-2a7d-436d-b11d-9ca38742186f'

response = http.request(request)
util.debug_msg(response.read_body,true)
