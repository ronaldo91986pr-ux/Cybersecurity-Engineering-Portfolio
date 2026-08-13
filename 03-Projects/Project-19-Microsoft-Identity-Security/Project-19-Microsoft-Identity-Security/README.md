# Project 19 — Microsoft Identity Security & Conditional Access

## Project Overview

This project explores Microsoft identity security controls using the Microsoft Entra admin center in a read-only organizational environment.

The objective was to understand how Microsoft Entra protects identities using Multifactor Authentication (MFA), Conditional Access, authentication controls, and Role-Based Access Control (RBAC).

No administrative settings or policies were modified.

## Security Areas Explored

- Microsoft Entra ID
- Multifactor Authentication (MFA)
- Conditional Access
- Authentication methods
- Administrative roles
- Identity security
- RBAC
- Least privilege

## Multifactor Authentication

Microsoft Entra MFA provides an additional authentication requirement beyond a password.

The Entra interface demonstrated that MFA can be integrated with Conditional Access to apply authentication requirements based on organizational access policies.

From a security assessment perspective, important discovery questions include:

- Is MFA deployed across the organization?
- Are privileged accounts protected with stronger authentication?
- Which authentication methods are permitted?
- Are legacy authentication methods still present?
- Are MFA requirements enforced through Conditional Access?

## Conditional Access

Conditional Access provides policy-based access control for organizational resources.

A typical access decision can consider signals such as:

User
↓
Application
↓
Device
↓
Location
↓
Authentication
↓
Risk
↓
Access Control

Possible controls can include:

- Require MFA
- Require stronger authentication
- Require compliant devices
- Restrict access
- Block access

## RBAC Observation

When attempting to access the Conditional Access configuration, the portal returned:

**HTTP 403 — Insufficient privileges to complete the operation**

This demonstrated that authentication to the tenant does not automatically grant authorization to manage security policies.

No attempt was made to elevate privileges or bypass the restriction.

## Security Assessment Perspective

When evaluating an organization's identity security posture, I would investigate:

1. How identities are managed.
2. Whether MFA is consistently enforced.
3. How privileged accounts are protected.
4. Which authentication methods are allowed.
5. Whether Conditional Access is implemented.
6. How devices influence access decisions.
7. Whether risky or abnormal authentication activity is monitored.
8. How administrative privileges are assigned and reviewed.
9. Whether least privilege is consistently applied.

## Example Customer Scenario

### Business Problem

A customer reports suspicious login attempts and inconsistent MFA adoption.

### Discovery

Questions would focus on:

- Identity architecture
- MFA coverage
- Privileged accounts
- Authentication methods
- Conditional Access
- Device management
- Security monitoring
- Access governance

### Potential Assessment Direction

**Microsoft Security Assessment**

The objective would be to identify potential identity and access-control gaps and determine appropriate next steps with the technical assessment team.

## Key Findings

- MFA strengthens authentication beyond passwords.
- Conditional Access provides policy-driven access decisions.
- Identity security depends on both authentication and authorization.
- RBAC restricts access to privileged security configuration.
- Least privilege reduces unnecessary administrative exposure.
- Security assessment discovery should connect technical controls to organizational risk.

## Skills Demonstrated

- Microsoft Entra ID
- Identity and Access Management (IAM)
- Multifactor Authentication
- Conditional Access concepts
- Authentication
- Authorization
- RBAC
- Least privilege
- Identity security assessment
- Customer security discovery

## Evidence

Read-only evidence collected included:

1. Microsoft Entra identity environment
2. Administrative role architecture
3. Account with no administrative roles
4. Restricted Sign-in Logs
5. Conditional Access — HTTP 403 authorization boundary
6. Microsoft Entra MFA interface

Public screenshots must be sanitized before publication to remove account information, tenant identifiers, organizational data, and other sensitive information.

## Ethical Controls

This project was conducted strictly within existing account permissions.

No policies, identities, authentication settings, roles, groups, applications, or tenant configurations were changed.

No privilege escalation was attempted.

## Conclusion

This project demonstrated the relationship between identity, authentication, authorization, MFA, Conditional Access, RBAC, and least privilege in Microsoft Entra.

It also demonstrated an important security principle: being authenticated to a Microsoft cloud environment does not mean a user is authorized to access or modify security-sensitive resources.
