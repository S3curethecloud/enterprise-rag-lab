# TechCorp Architecture Standards

## API Authentication

Production APIs must use approved identity-based authentication.

Static credentials should not be embedded in application source code.

## Encryption

Sensitive application traffic must use encrypted transport.

## Service Identity

Production workloads should use managed workload identities where supported.

## Logging

Security-relevant events must be forwarded to approved centralized logging systems.
