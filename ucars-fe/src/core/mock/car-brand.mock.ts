import { CarBrand } from "../models/car-brand.model";

export class CarBrandFaker {

    static fakeCarBrands = () => {
        let carBrands: Array<CarBrand> = [];
        for (let i = 1; i <= 10; i++) {
            const carBrand = new CarBrand({
              id: i,
              name: `Car Brand ${i}`,
              logo: '/assets/images/no-image.png',
              description: 'Brand desctiption to long so it will be hide. Brand desctiption to long so it will be hide. Brand desctiption to long so it will be hide.',
              count_models: 1000,
              updated_at: '2022-10-25',
              is_active: Boolean(i % 2),
            });
            carBrands.push(carBrand);
        }
        return carBrands;
    }
} 