export class BaseModel {
    public map(obj: any){
        const properties = Object.keys(this);
        let newObj: any = {}
        for (let index = 0; index < properties.length; index++) {
            const property = properties[index];
            if (Object.prototype.hasOwnProperty.call(obj, property)) {
                newObj[property] = obj[property];
            }
        }
        Object.assign(this, newObj);
    }
}