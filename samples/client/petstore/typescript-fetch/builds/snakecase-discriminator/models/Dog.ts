/* tslint:disable */
/* eslint-disable */
/**
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
import type { Animal } from './Animal';
import {
    AnimalFromJSON,
    AnimalFromJSONTyped,
    AnimalToJSON,
    AnimalToJSONTyped,
} from './Animal';

/**
 * 
 * @export
 * @interface Dog
 */
export interface Dog extends Animal {
    /**
     * 
     * @type {string}
     * @memberof Dog
     */
    breed?: string;
}

/**
 * Check if a given object implements the Dog interface.
 */
export function instanceOfDog(value: object): value is Dog {
    return true;
}

export function DogFromJSON(json: any): Dog {
    return DogFromJSONTyped(json, false);
}

export function DogFromJSONTyped(json: any, ignoreDiscriminator: boolean): Dog {
    if (json == null) {
        return json;
    }
    return {
        ...AnimalFromJSONTyped(json, true),
        'breed': json['breed'] == null ? undefined : json['breed'],
    };
}

  export function DogToJSON(json: any): Dog {
      return DogToJSONTyped(json, false);
  }

  export function DogToJSONTyped(value?: Dog | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        ...AnimalToJSONTyped(value, true),
        'breed': value['breed'],
    };
}

