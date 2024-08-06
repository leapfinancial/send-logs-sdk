# from lola_logs import LolaLogs
# from lola_logs_settings import LolaLogsSettings
# from logging import Logger

# if __name__ == "__main__":
#     config = LolaLogsSettings(
#         logger_name="lolalogs-test",
#         project_id="numichat",
#         topic_name="send_logs_sdk",
#         service_account_key='{"type": "service_account","project_id": "numichat","private_key_id": "eea7e5ee36afdb5bf2a8aa3109d58847b1f72b05","private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCJXQ/+7BQ8p6Wb\nT2dB++EBVwKjBB/dOI6Lc6smZasrOGPCl/VdevBj0Ys6rVtJKisxx3z8botkenJT\nZCF/DMyNPrlMDLpMPGU2bPTMbpD3YxgqV+AvB/YyOhaiDjBNWbh7VJqSvlLbnpGC\nfCgZmS6ipIVPGvmwT0SmjJGW02YCc7pQr3KFkDiQrL8AHGWhMFB3zee3sZDxXe4M\nQP9T7Qwh0q3akRpbiMCOhR84/SPTrtqPAuZwxU4b+H+8tezprEOOTu0qMkKV8qnC\n47pLYfyzjsME+Pu9hr0V/tQl9CD0eX+I2C9qxFV1x7HMNl/ag0nPUZWWxxGcr6HA\nl/PdEITXAgMBAAECggEALP6BzdPQsSmM8nmo7hEuW7z/jRw9v73V21HxHuuwjMC0\n1Lnn0k4BzgCGZZsBSs74RR7+DsW6/RequSwUWMR9gEqqcYG9yFkEIjbAXPJeo9oe\nwUf1lBI8j6k9XqndIokgB63nz+dtxqiDK0W18OSfRQE09Xt1jE36w79JtSjbwjNh\nTr57878MfjjRhBl6sUgi+dcaDHIMOfcronpk8XLwUTHOnPXx2bOAMZEumRYqB1cX\nhdfiBmABm4ILxDC6ugdmYbGMfBTY+Qj7GmOtWlqGLTrpcu9KaE2J/O7evlOmB7Tn\nWjE1BCdYgs3aE2+YP4htf/zaFXp7oVYvzLZ3uURckQKBgQDA7L9rQKoN9J+5rPA9\nGpCcEiB0usVFW6aG6YB2Zsfx7FC+pbSZrYaniWlc5Bp7yOrvRisE+UEeh/53UV/U\naBdwxDzp/31SOfESsqsAfDeajCdBLee98JGmq0Sj4agyyaJJXMCmvnYG0x0i/RDT\njc/qf/la9APbPDg/lzXEdWOMqQKBgQC2Rf7nILSykQQp11ELsYJafiW0fK1qywqi\nWVVw2eAFouWMbqH2tVylzA2sYsf6anbY/e+N0eLA58GEBaGw6gV9Eb38Fm4K3uYN\nj3qXm29mjqoN2EBFSFlQ6qziP87ajtW+fS1ays5yxGkT2yjLpSqQqem3dCnpYJ+h\nMB493JD1fwKBgFvfIhTIGXNF395C3bCretvnwe70lka+K2IpxhQcQ/EP8S+op4Vb\nXjlgNX2X3oi+GCrTxl669+i7KFHXvYPgAfGgccWY9iv3DbcywD4d6Ti+r17ZpncM\nHcA55RkJt9hfrtmywsdlAb2kQUbNLnsgGDf6s1s9wqxfVAXsUx14LWzpAoGAarDU\nAMPzISajMj6XcOnJbGC0f04PUBhjNB5oVbMiXwo3pRjI8xi7j0y+oC398kVJJcCV\n7QRy3wmJC1ckiuKgrdGpzBnw9an9LOjUEFPqRDSzs4DmNeegaC3FXnWNBf9fe63X\n03Isn576BqZc3b7jCGR8qmZzdeiZ54a73Ofzbc8CgYEAp4Xk0W0AvkguQGK8mVvk\nhB0YM/9AFsTiu0z84BOOd7adklBk0lSDi5JqryqLVKhAthJ6zdvXB5Slfp7JIaXi\n6pS8ukDauQCNCuuJS8EsDlNy5FOOAwMj93KGX54JA8aH8uml4nkeU3mGSWJuX2Fn\ngYt1grIBU28Dez78KdNjg/w=\n-----END PRIVATE KEY-----\n","client_email": "lolalogs-v2@numichat.iam.gserviceaccount.com","client_id": "111633855718629857466","auth_uri": "https://accounts.google.com/o/oauth2/auth","token_uri": "https://oauth2.googleapis.com/token","auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/lolalogs-v2%40numichat.iam.gserviceaccount.com","universe_domain": "googleapis.com"}'
#     )
#     lolaConfig = LolaLogs(config)
#     lola_logs = lolaConfig.set_global_tags({"test": "test"})    
#     lola_logs.info("logs info")
#     print("Logs enviados")
#     lola_logs.warning("logs warning")
#     print("Logs enviados")
#     lola_logs.error("logs error")
#     print("Logs enviados")
    