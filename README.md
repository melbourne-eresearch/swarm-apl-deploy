# SWARM Deployment

This [Ansbile](https://www.ansible.com/) playbook deploys SWARM stack to a Linux server that runs Ubuntu.

## Requirements

### Ansible

Ansbile is required to run this playbook. Please follow the instructions [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) to install Ansible to your local computer.

**Note:** This script has been tested on MacOS with Ansible version 2.7.5 only.

### Google OAuth 2.0

Google authorization credentials are required to use Google OAuth in SWARM (**optional**). Please follow the [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/OAuth2WebServer) guide to create the credentials.

### Microsoft OAuth 2.0

Microsoft authorization credentials are required to use Microsoft OAuth in SWARM (**optional**). Please follow the [Authorize access to Azure Active Directory web applications using the OAuth 2.0 code grant flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code) guide to create the credentials.

### Ansible vault password

Sensitive data (such as SSL certificate and passwords) are encrpyted with Ansible vault. Vault password is required to decrept these data during the deployment.

## Deployment

### Inventory

Please create / update the inventory file and add the destination host(s) in the inventory. Example:

#### hosts

```bash
[Server]
115.146.92.16
```

### Set host vars

Please create the host vars files. Example:

#### vault_ apl.yaml

**Note:** This file should ideally be encrypted by the Ansible vault for security reasons.

| Operation | Command                                |
|-----------|----------------------------------------|
| Encrypt   | `ansible-vault encrypt vault_apl.yaml` |
| Decrypt   | `ansible-vault decrypt vault_apl.yaml` |
| View      | `ansible-vault view vault_apl.yaml`    |
| Edit      | `ansible-vault edit vault_apl.yaml`    |

```yaml
# Haproxy
fqdn: swarm-apl.eresearch.unimelb.edu.au        # Fully qualified domain name
haproxy_admin: admin                            # Admin username (for access /haprxoy?stats and /upload/usergroup endpoints)
haproxy_admin_password: password                # Admin password

                                                # SSL sertificate, the example is a self-signed certificate, please replace it with a proper SSL certificate
ssl_cert: |
  -----BEGIN RSA PRIVATE KEY-----
  MIIEpAIBAAKCAQEA2+FqxKDl41Ywwp1l5zqy1vv5meOAnffwHEiE4+ikXYklmYpD
  B0BQdj8bTTe0rFiF2aG76Zx/jNlAqV3geDT+s4awtmpDDkTlDuIBaWen7ACWYJo8
  ABELiCha9CQJ5OoI3U5j9g03u/XeMb7f7at/kYTl7lr0c//UEzhVtv7gVBOsqlc3
  6hiZoo3ps0tk/QEpDNWm8fgyDw8IA5fZVLVc7hXx+OlxwOJwfC5Y7Mb49KVluwPS
  sOeRBLcF/LzejuBvPFPDwSG3dWRwdMGtSttn8j5faa8pkTqiUbg7ya9ngGtvYpzz
  XGxuTgJHMydCpK5knsy2TSgNovNUBpXUUDeiqwIDAQABAoIBAG9373CPQPvnDgEb
  WjXHBDMIupjRRLrQnuE3wmbn4aupg247MY/TgvbvNyAGRYm5tuGFpIXh2KfG24kB
  FnLaKuVIOv2/EQ+CzbylxqFw8ygphBKlHhXKjlYQX0u1mW57VtMakoKCYObg1ivR
  4CPU9W8IOKiFY7gK0bCMtqd2vrLf9ddEWsnLpYOvbNWONtlnca7VhxDPBKRfUZO7
  2mCuOqMM2Fny3d+ST1hYQmdmQx15Q0hmPQZ3efGfORYZq9NvnI+pJADtLaz1zfbm
  4hYjVmqZQ3xkXJlMbmsNhNQYuGdgyYRn2EiIMJBRqMRbewdWLwXDryRGZnKOywqL
  Z9fp9cECgYEA9GwmrI6gr1sT9D/HdD9m5z0S3RIH50U9FWYr2zoN88WCZsJu74WT
  Whs3rM8JmMytlgTw7Ug9L6z/0UrNLOZy7gA8rbX1mGUHB98KUkyjPPzSIY0Ztw9H
  oyjZBzxRcL2QR0pQN98UIJxL3R9gBsOMqXpAAq9w6j3Ok/y/t+S/YGUCgYEA5kus
  HwEst42Gh6DMhVzmLSy5MEZ24G3xVuIcbVVVJ4+1LJnxueAzS442RBEZFG5EnJjX
  /G1BB9Ropx+jXbk6xfir3LNSuFoAHxIyM2FMWfIogvsJQ+yVDmOl8MuFcR7BYh8x
  c03A5t8An4lME9oYX8I1oAOg/NyBDAhuObxkXc8CgYBblwNO+gtAapKpnhSxfOik
  kgA1kwIfKZTgJe8dMT31MPfSZd2IJ7e1tilAujxQY7JQWv2lDMLQ0LTzymHkB17d
  zHzwYxTqzEC8NFn7yPgKbHqZU/Rk4nbnrvDUg0fJRV+BN1mj9hXmumq7K3yiTDiz
  cTn3R6K6Q/ra/YUh9be4+QKBgQDSBDSFWdbj1YbX7QZWoK+whtajdb83UEwFBdMS
  yf0MRPveHs3YyuM8hgZq8ITEowKjJKfjpebmMwj1T971u9QjcnGYpVhMkpcFvtxV
  CuhMJpBXUoPSk9Ai/TD5dUDONlP5HaVFF6VRZhD1bIoamIwd18h7kpOfxZ9Rz+Zl
  dK669QKBgQCAH2L/TefG77JyOFeJD1g144qmUEOhAxveu2W4j7LFGfNhWSKUJJJI
  OdX5YEvsgWdH3AvI0ylFnC8MM2cnG46VgNjScgu5KBBjYDlDVsImg1iOP8HfvqaG
  ghREav9W3fLnZ3yzLem8NvZ4W5QTmq9oRRGFDRFUDwTNMaK+sQciuA==
  -----END RSA PRIVATE KEY-----
  -----BEGIN CERTIFICATE-----
  MIIDXjCCAkYCCQCy3E87UXO+dDANBgkqhkiG9w0BAQsFADBxMQswCQYDVQQGEwJB
  VTEMMAoGA1UECAwDVklDMRIwEAYDVQQHDAlNZWxib3VybmUxJDAiBgNVBAoMG1Ro
  ZSBVbml2ZXJzaXR5IG9mIE1lbGJvdXJuZTEMMAoGA1UECwwDTVNFMQwwCgYDVQQD
  DANNZUcwHhcNMTgxMjE3MDI1NDEwWhcNMjgxMjE0MDI1NDEwWjBxMQswCQYDVQQG
  EwJBVTEMMAoGA1UECAwDVklDMRIwEAYDVQQHDAlNZWxib3VybmUxJDAiBgNVBAoM
  G1RoZSBVbml2ZXJzaXR5IG9mIE1lbGJvdXJuZTEMMAoGA1UECwwDTVNFMQwwCgYD
  VQQDDANNZUcwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDb4WrEoOXj
  VjDCnWXnOrLW+/mZ44Cd9/AcSITj6KRdiSWZikMHQFB2PxtNN7SsWIXZobvpnH+M
  2UCpXeB4NP6zhrC2akMOROUO4gFpZ6fsAJZgmjwAEQuIKFr0JAnk6gjdTmP2DTe7
  9d4xvt/tq3+RhOXuWvRz/9QTOFW2/uBUE6yqVzfqGJmijemzS2T9ASkM1abx+DIP
  DwgDl9lUtVzuFfH46XHA4nB8Lljsxvj0pWW7A9Kw55EEtwX8vN6O4G88U8PBIbd1
  ZHB0wa1K22fyPl9prymROqJRuDvJr2eAa29inPNcbG5OAkczJ0KkrmSezLZNKA2i
  81QGldRQN6KrAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAF9zBn+kSV+6zAZu6mcf
  9NzGeXAju+ygAJA4B9CGtPXuwOCH1xCZPVajOhjBAlshUjU/419Ub4NzqTi5znsz
  0MkkzXdAa//8LT10lltGMQVpNPUZvl2kNtCrLWj7VPMRfysEL9u2GGPF19lDRzYV
  32g6BMQvZg7efkx3wWFU2uLM2p0R7SkO3c7PZ0fZLnS1aykvFkqaPbALPBoKGZsF
  KDnt+ZuBVpm94rnZI/cds2RM56VeDwjXl1ALikrC/hnRScXYGKd0t1AoeX7ScpUs
  CM83MfMOVF4GTw/DD3DXnWcgXMfY+3kXfx8jW3GfjhxPsIaSlUPU4NwPA7UlMyfh
  ec4=
  -----END CERTIFICATE-----

# AWS
aws_access_key_id: 'YOUR_ACCESS_KEY_ID'                                    # AWS access key ID
aws_secret_access_key: 'YOUR_SECRET_ACCESS_KEY'                            # AWS secret access key

# Volumes if there are any volumes attached to the VM
volumes:
  - device: /dev/vdb
    mountpoint: /var/lib/docker
  - device: /dev/vdc
    mountpoint: /data

# Volumes if there are not volumes attached to the VM
# volumes:
#   - mountpoint: /var/lib/docker
#   - mountpoint: /data

# UI
ui_container: ui                                                           # The name of the UI container
ui_image: ui:latest                                                        # UI Docker image

# API
api_container: api                                                         # The name of the API container
api_image: api:latest                                                      # API Docker image
swarm_version: '1.12.0'                                                    # SWARM version to display in the UI
rubric_aggregation: mean                                                   # The rubric aggregation model, currently only `mean` is valid

db_user: swarm                                                             # API database username
db_password: password                                                      # API database password
db_name: swarm                                                             # API database name
flask_secret_key: secret                                                   # Flask application secret key
google_id: 'Google ID'                                                     # Google ID (optional), for Google Oauth only
google_secret: 'Google secret'                                             # Google secret (optional), for Google Oauth only
zapier_application_key: ''                                                 # Zapier application key (optional), currently not in use

mail_username: sender@example.com                                          # Mail server username
mail_password: password                                                    # Mail server password
mail_default_receiver: receiver@example.com                                # The email address to receive the reports
swarm_admin_user: swarm-master                                             # SWARM admin username
swarm_admin_password: password                                             # SWARM admin password

azure_tenant_id: 'Azure tenant ID'                                         # Azure tenant ID (optional), for Microsoft Oauth only
azure_application_id: 'Azure application ID'    # Azure application ID (optional), for Microsoft Oauth only
azure_application_secret: 'Azure secret'                                   # Azure secret (optional), for Microsoft Oauth only
azure_super_user_id: 'Azure super user ID'                                 # User ID of the Azure super user, currently not in use
azure_super_user_onenote_folder_id: 'Azure super user Onenote folder ID'   # Azure super user Onenote folder ID, currently not in use
azure_super_user_word_template_id: 'Azure super user Word template ID'     # Azure super user Word template ID, currently not in use

# API Postgresql
api_db_container: postgres                                                 # The name of the API database container
api_db_volume: /data/database/pgdata                                       # The directory to persist the database files

api_db_root_password: password                                             # API Postgresql root password

# eJabberd Postgresql
ejabberd_db_container: postgres-ejabberd                                   # The name of the eJabberd database container
ejabberd_db_volume: /data/ejabberd/pgdata                                  # The directory to persist the database files

ejabberd_db_name: ejabberd                                                 # eJabberd database name
ejabberd_db_user: ejabberd                                                 # eJabberd database username
ejabberd_db_root_password: ejabberd                                        # eJabberd database root password

# eJabberd
ejabberd_container: apl-ejabberd                                           # The name of the eJabberd container
ejabberd_image: ejabberd:latest                                            # eJabberd Docker image
ejabberd_log_volume: /data/ejabberd/muclogs                                # The directory to save the eJabberd muclogs

ejabberd_db_password: ejabberd                                             # eJabberd database password

# Event service
es_container: eventservice                                                 # The name of the Event Service container
es_image: event-service:latest                                             # Event Service Docker image

es_db_name: eventservice                                                   # Event Service database name
es_db_user: eventservice                                                   # Event Service database username
es_db_password: eventservice                                               # Event Service database password
ns_webpush_private_key: 'Webpush Key'                                      # Private key for webpush service

# Notification
notification_containter: notification                                      # The name of the Notification container
notification_image: notification:latest                                    # Notification Docker image

notification_db_name: notification                                         # Notification database name
notification_db_user: notification                                         # Notification database username
notification_db_password: notification                                     # Notification database password
notification_fcm_key: 'FCM Key'                                            # FCM Key for Notification

# Report
report_container: report                                                   # The name of the Report container
report_image: report:latest                                                # Report Docker image

# Common
swarm_dir: /home/{{ ansible_user }}/swarm                                  # The directory to save the docker-compose file
```

### Run playbook

Use the command below to run the playbook, and only supply `--vault-id @prompt` if the `host-vars-file` is encrypted by Ansible vault. `-vvvv` option is for debug purpose only.

```bash
ansible-playbook [-vvvv] -i hosts -u ubuntu --key-file=<path-to-ssh-private-key> \
                 -e @./host_vars/<host-vars-file-name> [--vault-id @prompt] server.yaml
```