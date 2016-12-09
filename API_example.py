from sslblacklistAPI import SSLBlackList

res = SSLBlackList(True).retrieve_results()
print res

# res = SSLBlackList(True).search('1f0eddff3174fe3ebcfa4c625fe9f619a58e282e')
# print res
