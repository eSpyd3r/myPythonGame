import pygame

class Entity(pygame.sprite.Sprite):
	def __init__(self,groups):
		super().__init__(groups)
		self.frame_index = 0
		self.animation_speed = 0.15
		self.direction = pygame.math.Vector2()

	def move(self,speed):
		if self.direction.magnitude() != 0: #vectors of length 0 can't be normalized
			self.direction = self.direction.normalize() #accounting for moving in x and y at the same time; maintaining speed


		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center
		
	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: #in motion to the right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: #in motion to the left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: #in motion downwards
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: #in motion upwards
						self.hitbox.top = sprite.hitbox.bottom