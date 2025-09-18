package com.mainProject.fakenewsbackend

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class FakeNewsBackendApplication

fun main(args: Array<String>) {
    runApplication<FakeNewsBackendApplication>(*args)
}
