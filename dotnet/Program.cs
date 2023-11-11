var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("api/v1/products", () =>
{
    app.Logger.LogInformation("Starting to get products");

    var products = new Product[]
    {
        new Product
        {
            Id = "1",
            Name = "Product 1",
            Price = 9.99f
        },
        new Product
        {
            Id = "2",
            Name = "Product 2",
            Price = 19.99f
        }
    };

    app.Logger.LogInformation("Finished getting products");

    return Results.Ok(products);
});

app.Run();

class Product
{
    public string Id { get; set; } = default!;
    public string Name { get; set; } = default!;
    public float Price { get; set; }
}