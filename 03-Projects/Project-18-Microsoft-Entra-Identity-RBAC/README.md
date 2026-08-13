# Project 18 — Microsoft Entra ID: Identity, RBAC & Least Privilege

## Project Overview

This project documents a read-only exploration of Microsoft Entra ID identity and access management within an organizational Microsoft Entra environment.
`
The objective was to understand how Microsoft Entra manages identities, administrative roles, authentication information, security telemetry, and access restrictions while respecting the permissions assigned to my account.

No administrative changes were performed.

## Objectives

- Explore Microsoft Entra ID architecture
- Review user and group management interfaces
- Understand Member and Guest identity types
- Explore Microsoft Entra administrative roles
- Identify privileged vs non-privileged roles
- Investigate access to security-sensitive information
- Observe RBAC and least-privilege enforcement
- Understand authorization failures
- Document findings without modifying the environment

## Environment

- Microsoft Entra admin center
- Organizational Microsoft Entra tenant
- Microsoft Entra ID P2 environment
- Standard user account
- No administrative roles assigned

## Identity Management

The Microsoft Entra Users interface was reviewed to understand how identities are represented and managed.

Observed identity concepts included:

- User Principal Name (UPN)
- Member accounts
- Guest accounts
- On-premises synchronized identities
- User authentication management
- Password reset capabilities
- MFA management interfaces

No users were created, modified, deleted, or otherwise administered during this project.

## Role-Based Access Control

The Microsoft Entra **Roles and administrators** interface was reviewed.

Microsoft Entra uses administrative roles to delegate access to privileged actions.

The environment demonstrated separation between:

- Standard users
- Administrative roles
- Built-in roles
- Privileged roles
- Role assignments

My account had no administrative role assigned.

This demonstrated the principle of least privilege: access to an organizational tenant does not automatically provide administrative authority.

## Authorization Test

An attempt was made to view Microsoft Entra Sign-in Logs through the normal administrative interface.

The request returned:

**HTTP 401 — Unauthorized**

The portal indicated that additional administrator-granted access was required.

No attempt was made to bypass or elevate the existing permissions.

## Security Finding

The Microsoft Entra overview also restricted access to identity-risk information.

This demonstrated that security-sensitive telemetry is protected separately from general directory information.

## Security Principles Demonstrated

### Least Privilege

Users should receive only the permissions required to perform their responsibilities.

### Role-Based Access Control

Administrative capabilities are controlled through assigned Microsoft Entra roles.

### Separation of Duties

Access to directory information does not automatically provide access to security monitoring or privileged administrative functions.

### Identity Governance

Administrative privileges and sensitive identity information require additional authorization.

## Key Findings

- Microsoft Entra centralizes identity and access management.
- Member and Guest identities can coexist within a tenant.
- Administrative privileges are controlled through role assignments.
- Some Entra roles are explicitly classified as privileged.
- Standard tenant access does not imply administrative access.
- Sign-in telemetry can require additional permissions.
- Identity-risk information can be restricted.
- Unauthorized requests are denied rather than exposing sensitive telemetry.
- RBAC provides an important control for enforcing least privilege.

## Skills Demonstrated

- Microsoft Entra ID
- Identity and Access Management (IAM)
- Role-Based Access Control (RBAC)
- Least Privilege
- Identity Governance concepts
- Authentication concepts
- Microsoft cloud security
- Authorization troubleshooting
- Security documentation

## Evidence

Evidence collected during the lab included:

1. Microsoft Entra tenant overview
2. Users management interface
3. Restricted Sign-in Logs — HTTP 401
4. Account with no administrative roles
5. Roles and administrators interface
6. Built-in and privileged role architecture

Screenshots used publicly should be sanitized to remove tenant identifiers, account identifiers, user information, and other organizational information.

## Ethical and Access Controls

This project was performed strictly within the permissions granted to the account.

No privilege escalation was attempted.

No users, groups, roles, authentication settings, policies, applications, or tenant configuration were modified.

## Conclusion

This lab demonstrated how Microsoft Entra ID applies identity-based authorization and role-based access control within an organizational environment.

The most important observation was that authenticated access to Microsoft Entra does not automatically provide access to privileged administrative or security functions.

The environment enforced least privilege by restricting sensitive identity and sign-in information when the account lacked the required administrative permissions.
