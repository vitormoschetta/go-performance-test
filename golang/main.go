package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/vitormoschetta/go/pkg/middlewares"
)

func main() {
	router := mux.NewRouter()
	router.Use(middlewares.AcceptJSON)

	router.HandleFunc("/api/v1/products", func(w http.ResponseWriter, r *http.Request) {
		log.Println("Starting to get products")

		products := []Product{
			{ID: "1", Name: "Product 1", Price: 9.99},
			{ID: "2", Name: "Product 2", Price: 19.99},
		}
		json.NewEncoder(w).Encode(products)

		log.Println("Finishing to get products")
	}).Methods(http.MethodGet)

	fmt.Println("Server running on port 8080")
	err := http.ListenAndServe(":8080", router)
	if err != nil {
		log.Fatal(err)
	}
}

type Product struct {
	ID    string  `json:"id"`
	Name  string  `json:"name"`
	Price float64 `json:"price"`
}
