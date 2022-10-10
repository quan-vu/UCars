export class Utils {

    static randomInt(min: number, max: number) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min) + min);
    }

    static randomBool() {
        return Boolean(this.randomInt(0, 1));
    }
}