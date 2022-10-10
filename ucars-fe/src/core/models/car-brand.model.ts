import { BaseModel } from "./base.models";

export class CarBrand extends BaseModel {
    public id: number = 0;
    public name: string = '';
    public logo: string = '';
    public description: string = '';
    public count_models: number = 0;
    public updated_at: string = '';
    public is_active: boolean = false;

    constructor(obj: any) {
        super();
        this.map(obj);
    }
}