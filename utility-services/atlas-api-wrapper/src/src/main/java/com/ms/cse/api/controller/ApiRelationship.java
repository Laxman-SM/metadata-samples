package com.ms.cse.api.controller;


import java.io.IOException;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.ms.cse.api.exception.CustomAllException;
import com.ms.cse.api.service.ApiService;

@RestController
public class ApiRelationship {

	private static final Logger LOG = LoggerFactory.getLogger(ApiRelationship.class);
	@Autowired
	ApiService apiService;
	
	

	
	@PostMapping("/api/relationship")
	public String relationshipPost(@RequestBody String ipJSON) {
		try {
			return apiService.callApi("POST", ipJSON, "v2/relationship");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return e.getMessage();
		}
		
	}
	
	@PutMapping("/api/relationship")
	public String relationshipBulkPost(@RequestBody String ipJSON) throws IOException, Exception {
		try {
			return apiService.callApi("PUT", ipJSON, "v2/relationship");
		}	catch (CustomAllException e) {
			e.printStackTrace();
			 throw new CustomAllException(e.getLocalizedMessage());

		}
		
	}
	
	
	
	@GetMapping("/api/relationship/guid/{guid}")
	public String relationshipGUIDGet(@PathVariable String guid) throws IOException, CustomAllException {
		try {
			return apiService.callGuidApi("GET", "v2/relationship/guid/"+guid);
		}	catch (CustomAllException e) {
			e.printStackTrace();
			 throw new CustomAllException(e.getLocalizedMessage());

		}
		
	}
	
	@DeleteMapping("/api/relationship/guid/{guid}")
	public String relationshipGUIDDelete(@PathVariable String guid) throws IOException, CustomAllException {
		try {
			return apiService.callGuidApi("DELETE", "v2/relationship/guid/"+guid);
		}	catch (CustomAllException e) {
			e.printStackTrace();
			 throw new CustomAllException(e.getLocalizedMessage());

		}
		
	}
	
	
	
	
}