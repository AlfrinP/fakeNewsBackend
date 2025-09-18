package com.mainProject.fakenewsbackend.user

import org.springframework.data.relational.core.mapping.Table

@Table(name = "users")
class User {
    val id: Long? = null
    val userName: String? = null
    val password: String? = null
    val email: String? = null
    val roles: String? = null

}